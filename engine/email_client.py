import imaplib
import smtplib
import email
from email.header import decode_header
from engine.speech import speak
from engine.listen import take_command
from engine.ai import ask_ai

EMAIL_USER = "YOUR_EMAIL@gmail.com" 
EMAIL_PASS = "YOUR_APP_PASSWORD" 

def check_emails():
    if "YOUR_EMAIL" in EMAIL_USER:
        speak("Sir, you haven't configured your email credentials yet. Please check the code.")
        return

    speak("Checking for new emails...")
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        status, messages = mail.search(None, '(UNSEEN)')
        email_ids = messages[0].split()

        if not email_ids:
            speak("You have no new emails, Sir.")
            mail.close()
            mail.logout()
            return
            
        latest_ids = list(reversed(email_ids[-5:]))
        speak(f"You have {len(email_ids)} new emails. Reading the latest one.")
        
        for idx, i in enumerate(latest_ids):
            res, msg = mail.fetch(i, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                        
                    sender, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(sender, bytes):
                        sender = sender.decode(encoding if encoding else "utf-8")

                    speak(f"Email from {sender}.")
                    speak(f"Subject: {subject}")
                    
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = msg.get_payload(decode=True).decode()

                    if body:
                        short_body = body[:2000] 
                        ask_ai(f"Summarize this email from {sender} in one sentence: {short_body}")
                    
                    speak("Do you want to reply?")
                    choice = take_command()
                    if "yes" in choice or "sure" in choice or "reply" in choice:
                        send_reply_flow(sender, subject)
                    
                    if idx < len(latest_ids) - 1:
                        speak("Do you want to read the next email?")
                        read_next = take_command()
                        if "yes" in read_next or "sure" in read_next or "next" in read_next:
                            continue 
                        else:
                            speak("Okay, closing inbox.")
                            mail.close()
                            mail.logout()
                            return 
                    else:
                        speak("That was the last new email.")

        mail.close()
        mail.logout()
        
    except Exception as e:
        print(f"Email Error: {e}")
        speak("I encountered an error accessing your emails.")

def send_reply_flow(recipient, original_subject):
    speak("What should I say?")
    content = take_command()
    if content == "None":
        speak("Cancellation confirmed.")
        return

    speak("Drafting response...")
    
    speak(f"You said: {content}. Sending now?")
    confirm = take_command()
    if "yes" in confirm or "send" in confirm:
        send_email(recipient, f"Re: {original_subject}", content)
    else:
        speak("Cancelled.")

def send_email(to_address, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_USER, to_address, message)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        print(f"Send Error: {e}")
        speak("Failed to send email.")
