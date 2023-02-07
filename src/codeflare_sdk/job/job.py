from abc import abstractclassmethod, ABCMeta

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..cluster.cluster import Cluster

class JobDefinition():
    @abstractclassmethod
    def submit(self, c: "Cluster") -> "Job":
        pass

class Job(metaclass=ABCMeta):
    @abstractclassmethod
    def status(self):
        pass

    @abstractclassmethod
    def logs(self, follow=False):
        pass

class TorchJobDef(JobDefinition):
    def __init__(self, requirements_file: str, script_file: str, gpus: int):
        pass

    def submit(c: "Cluster") -> "TorchJob":
        pass

class TorchJob(Job):
    def __init__(self, cluster: "Cluster", id: str):
        self.cluster = cluster
        self.id = id

    def status(self):
        pass

    def logs(self, follow=False):
        pass
