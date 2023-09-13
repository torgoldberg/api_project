import logging as logger
import random
import string
from phone_gen import PhoneNumber
from mimesis import Internet
import bcrypt


class GenericUtilities(object):

    @staticmethod
    def generate_random_email(domain=None, email_prefix=None):
        """
        Generate a random email
        """
        if not domain:
            domain = 'gmail.com'
        if not email_prefix:
            email_prefix = 'test'

        random_email_string_length = 10
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
        random_email = email_prefix + '_' + random_string + '@' + domain
        logger.debug(f"Randomly generated email: {random_email}")

        return random_email

    @staticmethod
    def generate_random_string(length=10, prefix=None, suffix=None):
        """
        Generate a random string
        """
        random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

        if prefix:
            random_string = prefix + random_string
        if suffix:
            random_string = random_string + suffix
        logger.debug(f"Randomly generated string: {random_string}")

        return random_string

    @staticmethod
    def generate_random_integer(length=10):
        """
        Generate a random integer
        """
        random_integer = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, length)])
        logger.debug(f"Randomly generated integer: {random_integer}")

        return random_integer

    @staticmethod
    def generate_random_phone_number(phone_number=None):
        """
        Generate a random phone number
        """
        if not phone_number:
            random_phone_number = PhoneNumber("ISR")
            phone_number = random_phone_number.get_number()
        logger.debug(f"Randomly generated phone number: {phone_number}")

        return phone_number

    @staticmethod
    def generate_random_ip_address(ip_address=None):
        """
        Generate a random ipv4 address
        """
        if not ip_address:
            ip_address = Internet().ip_v4()
        logger.debug(f"Randomly generated ipv4 address: {ip_address}")

        return ip_address

    @staticmethod
    def generate_random_password_hash(password_hash=None, length=None):
        """
        Generate a random password hash
        """
        if not password_hash:
            password = GenericUtilities.generate_complicated_word(length=length)
            salt = bcrypt.gensalt(rounds=4)
            password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)
            password_hash = str(password_hash)
        logger.debug(f"Randomly generated password hash: {password_hash}")

        return password_hash
