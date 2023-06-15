# Influencer Insta

This is the Python version of the t_rex_website repository (similar project but it is written in JS and displays the result as a website).

I used three different APIs to determine the basis for a prompt. The API chosen for this part is randomly selected.

The topic (ex: butterfly catching) is then fed into OpenAI's API to get a picture and appropriate caption.

- **Bucket List**: https://api-ninjas.com/api/bucketlist
- **Historical Events**: https://api-ninjas.com/api/historicalevents
- **Hobbies**: https://api-ninjas.com/api/hobbies

## Run Locally

- python3.9 -m venv "env"
- source env/bin/activate
- pip install -r requirements.txt

## Example Output

![T.Rex Image](img.jpg)

**Category:**  hobbies

**Prompt:** Create a long form Instagram post in the tone of an influencer who is describing what she did today.

Topic: Stone collecting

**Caption:** Today was a great day! I went stone collecting and it was so much fun! I got some really cool stones that I can’t wait to show off. I drove out to this spot that I know is usually good for finding beautiful stones. Once I got there I couldn’t believe my eyes! There were so many colors and shapes that it was hard to choose which ones to pick up. I eventually decided and got some of the smoothest stones I’ve ever seen. I’m so happy with what I collected and can’t wait to show them off! That’s why I love going stone collecting - it’s always such an amazing experience! #stonelover #stones #stonecollecting #outdoors #nature #collecting

**Url:**  https://oaidalleapiprodscus.blob.core.windows.net/private/org-7OpZvE448lNOat6zJ57DAFFb/user-s7sYaEG8wuA5J1xtFfnkfg88/img-eBR25Lbu14EeKyd3N9uDNMFr.png?st=2023-06-15T19%3A10%3A15Z&se=2023-06-15T21%3A10%3A15Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-06-14T21%3A20%3A46Z&ske=2023-06-15T21%3A20%3A46Z&sks=b&skv=2021-08-06&sig=cJzs5ksE1BqicMc7Ycd3gek4EJK3E8HFe%2BwwwmorxCQ%3D
