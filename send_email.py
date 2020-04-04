#https://gist.github.com/nickoala/569a9d191d088d82a5ef5c03c0690a02

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_ssl_host = '127.0.0.1'
smtp_ssl_port = 1025
username = 'sender@gmail.com'
password = 'smtp password'
recipient = "recipiento@gmail.com"

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April', 
    5: 'May', 
    6: 'June', 
    7: 'July',
    8: 'August', 
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_ssl_host = '127.0.0.1'
smtp_ssl_port = 1025
username = 'aadi@noahrei.com'
password = 'nIECeJV1k2hmwTh3NppfJA'
you = "aadi.kalloo@gmail.com"

lead_data = pd.read_csv('/Users/aadi/Documents/200124NVCLARK.csv')
ld = lead_data[['PRFirstName', 'PREmail', 'ProbateState', 'ProbateDate']]
ld = ld[~ld.PREmail.isna()]

for i in range(ld.shape[0]):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Please Read -- We are here to help :)"
    msg['From'] = username
    #you = ld.PREmail.iloc[i]
    msg['To'] = you
    print(i, ld.PRFirstName.iloc[i], ld.PREmail.iloc[i])

    text = """
        Hi {first_name},\n
        My wife, Olivia, and I found your contact info from a legal filing (public record) made in {filing_month} {filing_year} with the {filing_state} courts.\n
        We specialize in helping people solve any real estate-related problems they might have. If you need to sell a property quickly, we can definitely help by providing you with a cash offer and a quick closing.\n
        If you are not looking to sell a property at this point in time, please keep us in mind for the future.\n
        The number below is my direct line. Feel free to reach out to me at any time and please let me know if we can be of assistance in any way at all.\n
    """.format(email_signature=email_signature,
               filing_month=months[pd.to_datetime(ld.ProbateDate.iloc[i]).month],
               filing_year = pd.to_datetime(ld.ProbateDate.iloc[i]).year,
               filing_state = states[ld.ProbateState.iloc[i]],
               first_name= ld.PRFirstName.iloc[i],
              )

    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi {first_name},</p>
        <p>My wife, Olivia, and I found your contact info from a legal filing (public record) made in {filing_month} {filing_year} with the {filing_state} courts. </p>
        <p>We specialize in helping people solve any real estate-related problems they might have. If you need to sell a property quickly, we can definitely help by providing you with a cash offer and a quick closing.</p>
        <p>If you are not looking to sell a property at this point in time, please keep us in mind for the future.</p>
        <p>The number below is my direct line. Feel free to reach out to me at any time and please let me know if we can be of assistance in any way at all.</p>
        <p>Best,<br>Aadi</p>
        {email_signature}
      </body>
    </html>
    """.format(email_signature=email_signature,
               filing_month=months[pd.to_datetime(ld.ProbateDate.iloc[i]).month],
               filing_year = pd.to_datetime(ld.ProbateDate.iloc[i]).year,
               filing_state = states[ld.ProbateState.iloc[i]],
               first_name= ld.PRFirstName.iloc[i],
              )

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    server = SMTP(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, you, msg.as_string())
    server.quit()
    sleep(1)
