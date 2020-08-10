

def _concat_query_string(k, v):
    return '%s=%s&' % (str(k), str(v))


def create_url(url, *args, **kwargs) -> str:
    """
    Helper for generating Crate URLs
    :param args: The URI route from within Crate
    :param kwargs: Optional query string arguments
    :return: Full URL
    """
    for arg in args:
        url += '/%s' % arg

    if kwargs:
        url += '?'
        for k, v in kwargs.items():
            url += _concat_query_string(k, v)
    return url[:-1] if url[-1] == '&' else url