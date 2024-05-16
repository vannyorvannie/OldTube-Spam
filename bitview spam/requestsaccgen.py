import requests
import random 
import string
def generate_username(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_password(length=12):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
def generate_random_email(username_length=8):
    username = ''.join(random.choice(string.ascii_letters) for _ in range(username_length))
    email = f"{username}@gmail.com"
    return email




def genthiscrap(passwd, email, usrname):

    url = "https://www.bitview.net/signup"
    headers = {
        "authority": "www.bitview.net",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "PHPSESSID=egm1n9q4oqg3ls7pkdq1skbmq7",
        "origin": "https://www.bitview.net",
        "referer": "https://www.bitview.net/signup",
        "sec-ch-ua": '"Chromium";v="118", "Opera";v="104", "Not A?Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
    }

    data = {
        "email": f"{email}",
        "password": f"{passwd}",
        "password_again": f"{passwd}",
        "username": f"{usrname}",
        "g-recaptcha-response": "P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQSOXmimVfQ0WGwCFutEpZ_EnBYLekqEd1d4nvHPFVeyJiv0_VuaDfwW69ldmzmLoWAJSztazwgbL_N7zkLx_dSPit2me5hDdvYMov8e0JiE6kv9NjkEGg0Gpuj-2bLcbUBzHKGq5trwYTN0_hr448Lpbj0r7JCImQfG7m0UgkSw1TD2MLQn7vCuk4ElbsPGpT72WzmfqihACz61zuYpGL5YkZBzNn7n04beVnrCpBlZpzhhfqpUNkDG2ufbQFWnFLL3d9ZoN5VgGbBTfbatZXa6B9zDtq3KNtnrcdEQcHxErazxJ8L3TBbfGn7HKIEQ68ohTZFlihVnXQklLq9Zd6vmAlxbfZF0RPc8ko_trPHC_B59PkU8IOsfGq71MGwNw_07N_Fo5DNDRVBRMQLhHYmcNhOaVXtja5NkD-hladqYQUZU6sm8nXahgR-wc4Q7dyc8-B2ffUtx5pWOJPgDbTYFq0N1AuubiiljToAnVauDy2XTWk9BjtqTNlYvvznxSEL_Vt3vb6MiumDH_qtpVn3RkcIInAa4g8_D7SpTp0SxKom3LuMIMRRrx1yUYVHZG-5ijBh5tewf8y2s2_CjXus2K3mfzOqfoNXBvrBf_YshcvK88wabOgGRgrk63_LhZmWSn8Mtmdba2rE-uRzQa9KgibeZSPxkH7n9bv9zcwLj3gooaAtQgtugCOCqzxELzISG6h03d0fVX5c0nlcMhzzmZuXUcqmHH451J9GphOfySzidDk1XpJGkB4tEd_wUZttmbNhx6yFEywIYWYDKRsyjXhJjMDKIQ-C5fIAZDhS3r3GCdZMTk5W_jVl7yfZNEaM8GfEY5mDMTn7FhWToLAM1-_8AvmhMjEzPv2TB-fseMdwyKJbJtKqAZJEdTf6VOi1eqzXi44g10Ji9stdG_Zy1sT0Ji0HY9mI8V8dXTUcsoD0kSUVxB5xW9zVXZkNzcqw5g_rB9Vopz0QpYYsGllnkIRbiupE0stWw48ZboIu22K7i5hQX5jLSPnJIF6KzHEYfgLVq22q_4BAfwA1qI-S5Tph6StYN4AG8baJvC4aRzK32v2PqFAncifT-yXNGhtFWye0XzdOeExgi53ehrQGhSyBsAXtGQGgEefuj5rIEv4f0FO9_z5EO4nT5Hqmp7yfmR62naizhSUClYFvIB9zJ4jGAiFofLQw76yB-B0mZNfK3yYAbh4pHj5VTgaPRki2yuoAVvMaqy16b9Yo2bcWMoNyJ295O-UOpAeqwuBceOrpXrm2c8YYDZ3osg7bzzfrxxiD1kAJd1shV5IMtvukrBbgmem34eTsMehNCkK2SOwJTUkoePRP-iCxe5rkcPHaMlLgytwv8WtaOQ6MZZuM89ush-ftYP33XAYDzsxeP-pPYzfn1YO383pweZpjB8ej0UfeaDZtFJ9T9vaQ36zDn6cT5XiIgnQISqT76t1s1QW25lg69sLrYo172MjnSxqQqtn8cNg0InsqXY4svBdrW7Qi0YgyuD9DXmn7nJDjrVFO_-QB4R-HoEtS8D5nYO1pmd9vLf6pkSnND5wV4lIqjZXhwzmVlHh2oc2hhcmRfaWTOFZnkVKJwZAA.LAgUWAGJwKdEMnEUohktPzTt3q0YhN4Nb1cUJAX9Il0",
        "h-captcha-response": "P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQSOXmimVfQ0WGwCFutEpZ_EnBYLekqEd1d4nvHPFVeyJiv0_VuaDfwW69ldmzmLoWAJSztazwgbL_N7zkLx_dSPit2me5hDdvYMov8e0JiE6kv9NjkEGg0Gpuj-2bLcbUBzHKGq5trwYTN0_hr448Lpbj0r7JCImQfG7m0UgkSw1TD2MLQn7vCuk4ElbsPGpT72WzmfqihACz61zuYpGL5YkZBzNn7n04beVnrCpBlZpzhhfqpUNkDG2ufbQFWnFLL3d9ZoN5VgGbBTfbatZXa6B9zDtq3KNtnrcdEQcHxErazxJ8L3TBbfGn7HKIEQ68ohTZFlihVnXQklLq9Zd6vmAlxbfZF0RPc8ko_trPHC_B59PkU8IOsfGq71MGwNw_07N_Fo5DNDRVBRMQLhHYmcNhOaVXtja5NkD-hladqYQUZU6sm8nXahgR-wc4Q7dyc8-B2ffUtx5pWOJPgDbTYFq0N1AuubiiljToAnVauDy2XTWk9BjtqTNlYvvznxSEL_Vt3vb6MiumDH_qtpVn3RkcIInAa4g8_D7SpTp0SxKom3LuMIMRRrx1yUYVHZG-5ijBh5tewf8y2s2_CjXus2K3mfzOqfoNXBvrBf_YshcvK88wabOgGRgrk63_LhZmWSn8Mtmdba2rE-uRzQa9KgibeZSPxkH7n9bv9zcwLj3gooaAtQgtugCOCqzxELzISG6h03d0fVX5c0nlcMhzzmZuXUcqmHH451J9GphOfySzidDk1XpJGkB4tEd_wUZttmbNhx6yFEywIYWYDKRsyjXhJjMDKIQ-C5fIAZDhS3r3GCdZMTk5W_jVl7yfZNEaM8GfEY5mDMTn7FhWToLAM1-_8AvmhMjEzPv2TB-fseMdwyKJbJtKqAZJEdTf6VOi1eqzXi44g10Ji9stdG_Zy1sT0Ji0HY9mI8V8dXTUcsoD0kSUVxB5xW9zVXZkNzcqw5g_rB9Vopz0QpYYsGllnkIRbiupE0stWw48ZboIu22K7i5hQX5jLSPnJIF6KzHEYfgLVq22q_4BAfwA1qI-S5Tph6StYN4AG8baJvC4aRzK32v2PqFAncifT-yXNGhtFWye0XzdOeExgi53ehrQGhSyBsAXtGQGgEefuj5rIEv4f0FO9_z5EO4nT5Hqmp7yfmR62naizhSUClYFvIB9zJ4jGAiFofLQw76yB-B0mZNfK3yYAbh4pHj5VTgaPRki2yuoAVvMaqy16b9Yo2bcWMoNyJ295O-UOpAeqwuBceOrpXrm2c8YYDZ3osg7bzzfrxxiD1kAJd1shV5IMtvukrBbgmem34eTsMehNCkK2SOwJTUkoePRP-iCxe5rkcPHaMlLgytwv8WtaOQ6MZZuM89ush-ftYP33XAYDzsxeP-pPYzfn1YO383pweZpjB8ej0UfeaDZtFJ9T9vaQ36zDn6cT5XiIgnQISqT76t1s1QW25lg69sLrYo172MjnSxqQqtn8cNg0InsqXY4svBdrW7Qi0YgyuD9DXmn7nJDjrVFO_-QB4R-HoEtS8D5nYO1pmd9vLf6pkSnND5wV4lIqjZXhwzmVlHh2oc2hhcmRfaWTOFZnkVKJwZAA.LAgUWAGJwKdEMnEUohktPzTt3q0YhN4Nb1cUJAX9Il0",
        "terms_agreed": "on",
        "signIn": "Create my account",
    }

    response = requests.post(url, headers=headers, data=data)

    #print(response.text)
    print(response.status_code)
    with open("request.txt", "a") as file:
        file.write(f"{usrname}:{passwd}:{email}\n")


def dfjghdf(ass):
    url = "https://www.bitview.net/my_videos_upload"

    headers = {
        "authority": "www.bitview.net",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "multipart/form-data; boundary=----WebKitFormBoundarynkzKQFfIMOjluuFu",
        "cookie": "PHPSESSID=kq424iff81e34vspujkqrgulq7",
        "origin": "https://www.bitview.net",
        "referer": "https://www.bitview.net/my_videos_upload",
        "sec-ch-ua": '"Chromium";v="118", "Opera";v="104", "Not=A?Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"
    }

    data = f'''------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="title"

    {ass}
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="description"

    dfgdfgdgd
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="tags"

    dfgdfgdf
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="category"

    1
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="day"

    0
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="month"

    0
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="year"

    0
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="address"

    ------
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="country"

    ---
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="upload_video2"

    ------
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="video_file"; filename="Snaptik.app_7295390267643890976.mp4"
    Content-Type: video/mp4


    ------
    ------WebKitFormBoundarynkzKQFfIMOjluuFu
    Content-Disposition: form-data; name="broadcast"

    1
    ------WebKitFormBoundarynkzKQFfIMOjluuFu--
    '''

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)


if __name__ == "__main__":
    """
    for i in range(10):
        gennedpwd = generate_password()
        gennedusr = generate_username()
        gennedemil = generate_random_email()
        genthiscrap(email=gennedemil, passwd=gennedpwd, usrname=gennedusr)
    """
    while True:
        gennedpwd = generate_password()
        dfjghdf(gennedpwd)