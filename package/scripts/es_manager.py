#!/use/bin/env python
# coding = utf-8

from resource_management import *


def conf():
    import params
    # WARNING: You must specify that the group is elasticsearch, if not will start fail.
    dircreated = [params.elastic_dir,
                  params.pid_dir,
                  params.path_data,
                  params.log_dir,
                  params.elastic_home]

    Directory(dircreated,
              owner=params.elastic_user,
              group=params.elastic_group,
              create_parents=True
              )

    File(params.elastic_conf,
         owner=params.elastic_user,
         group=params.elastic_group,
         content=Template("elasticsearch.yml.j2")
         )

    File(format("{pid_dir}/es.pid"),
         owner=params.elastic_user,
         group=params.elastic_group
         )
