#!/usr/bin/env python

from resource_management import *


class ServiceCheck(Script):
    def service_check(self, env):
        import params
        env.set_params(params)

        Execute(params.check_es,
                logoutput=True,
                tries=3,
                try_sleep=20)


if __name__ == "__main__":
    ServiceCheck().execute()
