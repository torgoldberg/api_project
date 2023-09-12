import os
import logging as logger


class TenantUtilities(object):

    @staticmethod
    def get_tenant():
        """
        Get the tenant from the env.sh file and verify it exist in the file
        """
        tenant = os.environ['TENANT']
        logger.debug(tenant)
        if not tenant:
            raise Exception(f"The tenant must be in env file variables")

        return tenant
