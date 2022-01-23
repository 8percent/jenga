# 새로운 기능을 추가할 때마다 비용이 증가 한다.


def a():
    """Original Action since 2019"""
    pass


def b():
    """Additional action since 2020"""
    pass


def c():
    """Additional action since 2021"""
    pass


# 2019
# 잘 작동하는 상태

# API for web
def api_x():
    a()


# API for app
def api_y():
    a()


# API for internal product
def api_z():
    a()


# 2020
# 새로운 기능 B가 추가 되었음

# API for web
def api_x():
    a()
    b()


# API for app
def api_y():
    a()
    b()


# API for internal product
def api_z():
    """"""
    a()
    b()


# 2021
# 새로운 기능 C가 추가 되었음

# API for web
def api_x():
    a()
    b()
    c()


# API for app
def api_y():
    a()
    b()
    c()


# API for internal product
def api_z():
    """"""
    a()
    b()
    # 실수로 누락한 C 기능 호출
