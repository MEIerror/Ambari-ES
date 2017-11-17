# coding=utf-8
from resource_management import *
from resource_management.core import shell
from resource_management.core.resources.system import Execute, File
from resource_management.libraries.functions import format
from resource_management.libraries.functions.check_process_status import check_process_status



class Elasticsearch(Script):
    def install(self, env):
        import params
        env.set_params(params)
        Execute(format(
            "sh {service_packagedir}/files/downfiles.sh {es_tar_url} {work_dir} {elastic_user}"),
            logoutput=True
            )

    def configure(self, env):
        import params
        import es_manager
        env.set_params(params)
        es_manager.conf()


    def stop(self, env):
        import params
        import status_params
        env.set_params(params)
        cmd = format("lsof -i:{params.http_port}|grep {params.elastic_user}") + "| awk 'NR==1 {print $2}'"
        code, output = shell.call(cmd)
        if output:
            Execute("kill -9 " + output + " >/dev/null 2>&1", logoutput=True)

        File(status_params.pid_file,
             action="delete"
            )

    def start(self, env):
        import params
        import status_params
        env.set_params(params)
        env.set_params(status_params)
        self.configure(env)
        start_cmd = format("sh {service_packagedir}/files/start-es.sh {elastic_dir} {pid_dir}")
        Execute(start_cmd,
                logoutput=True,
                environment={
                    'JAVA_HOME': params.java_home,
                    'PATH': '$PATH:$JAVA_HOME/bin'
                }
                )

    def status(self, env):
        import status_params
        env.set_params(status_params)
        check_process_status(status_params.pid_file)


if __name__ == "__main__":
    Elasticsearch().execute()
