from distutils.core import setup, Command
from unittest import TextTestRunner, TestLoader

class TestCommand(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        tests = TestLoader().loadTestsFromNames(['nasadata.test.test_isstle'])
        t = TextTestRunner(verbosity = 1)
        t.run(tests)

setup(
    name='nasadata',
    version='0.1.0',
    author='Nathan Bergey',
    author_email='nathan.bergey@gmail.com',
    packages=['nasadata', 'nasadata.test'],
    license='LICENSE.txt',
    description='Unified scraper for NASA spaceflight data',
    long_description=open('README.txt').read(),
    cmdclass = {'test': TestCommand}
)
