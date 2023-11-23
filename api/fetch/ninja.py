from api.const.url import get_url_ninja_get_character

def fetch_ninja_character(url: str):
    """
    url is the ninja url
    i.e https://poe.ninja/challenge/builds/char/iwearbeanies/BeaniesBro_Divine_Focus?i=0
    """
    last_line_index = url.rindex('/')
    name = url[last_line_index+1:url.rindex('?')] if url.rindex('?') > last_line_index else url[last_line_index+1:]
    account = url[url.rindex('/', 0, last_line_index)+1:last_line_index]
    print(name, account)
    