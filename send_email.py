from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_ssl_host = '127.0.0.1'
smtp_ssl_port = 1025
username = 'sender@gmail.com'
password = 'smtp password'
recipient = "recipiento@gmail.com"

email_signature = """

<div class="protonmail_signature_block">
    <div class="protonmail_signature_block-user">
        <table style="border-spacing:0px;border-collapse:collapse;color:rgb(68,68,68);font-family:'Open Sans', sans-serif;font-size:14px;width:450px;" cellspacing="0" cellpadding="0" width="450">
            <tbody style="vertical-align:top;">
                <tr>
                    <td style="padding:0px 0px 10px;border-bottom:1px solid rgb(74,100,129);vertical-align:bottom;font-family:Verdana, sans-serif;color:rgb(59,73,8);" valign="bottom">
                        <div><b><span class="colour" style="color:rgb(74, 100, 129)"><span class="size" style="font-size:14pt">Aadi&nbsp;Kalloo</span></span></b>
                            <br>
                        </div>
                        <div><span class="colour" style="color:rgb(68, 68, 68)"><span class="size" style="font-size:10pt"><span class="colour" style="color:rgb(44, 44, 44)">Owner</span></span>
                            </span>
                            <br>
                        </div>
                    </td>
                    <td style="padding:0px 0px 10px;border-bottom:1px solid rgb(74,100,129);vertical-align:top;font-family:Verdana, sans-serif;color:rgb(59,73,8);" valign="top">
                        <a style="background-color:transparent;color:rgb(51,122,183);" href="https://www.noahrei.com/"><img style="border:0px;vertical-align:middle;width:179px;height:auto;" src="https://s3.amazonaws.com/reibb-users-media-library/u106925/wp-content/uploads/sites/5/2019/10/3_cropped1.png" width="179" alt="Logo" border="0"></a>
                        <br>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px 0px 0px;width:270px;line-height:18px;vertical-align:top;font-family:Verdana, sans-serif;font-size:10pt;" width="60%" valign="top"><span class="colour" style="color:rgb(44, 44, 44)"><span class="size" style="font-size:10pt">t: (443) 296-2871<span><br></span>e: <a href="mailto:team@noahrei.com">aadi@noahrei.com</a>
                        <br>w:&nbsp;</span>
                        </span><span><b><a href="http://www.noahrei.com/" style="background-color:transparent;color:rgb(51,122,183);"><span class="colour" style="color:rgb(59, 73, 8)"><span class="font" style="font-family:Verdana, sans-serif"><span class="size" style="font-size:10pt"><span class="colour" style="color:rgb(74, 100, 129)">www.noahrei.com</span></span>
                        </span>
                        </span>
                        </a>
                        </b>
                        </span>
                    </td>
                    <td style="padding:10px 0px 0px;width:180px;line-height:18px;vertical-align:top;font-family:Verdana, sans-serif;font-size:10pt;" width="40%" valign="top"><span class="colour" style="color:rgb(44, 44, 44)"><span class="size" style="font-size:10pt">50 W Broadway <br>STE 333 #28616 <br>Salt Lake City UT 84101</span></span>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px 0px 0px;width:270px;vertical-align:top;" valign="top" width="60%">
                        <br>
                    </td>
                    <td style="padding:10px 0px 0px;width:180px;vertical-align:top;" valign="top" width="40%">
                        <br>
                    </td>
                </tr>
            </tbody>
        </table>
        <div>
            <br>
        </div>
    </div>
    <div class="protonmail_signature_block-proton protonmail_signature_block-empty">
        <br>
    </div>
</div>

"""

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Yo"
msg['From'] = username
msg['To'] = recipient

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
    {email_signature}
  </body>
</html>
""".format(email_signature=email_signature)

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
server = SMTP(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(username, recipient, msg.as_string())
server.quit()
