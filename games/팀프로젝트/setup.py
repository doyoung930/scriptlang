from distutils.core import setup, Extension

module_spam = Extension('spam',
sources = ['spammodule.c'])

setup(
    name='SearchSports',
    version='1.0',

    py_modules=['스언어팀플', 'teller', 'noti'],
    packages=['icon'],
    package_data={'icon':['*.png']},

    ext_modules=[module_spam]
)