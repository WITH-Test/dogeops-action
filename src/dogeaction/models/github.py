from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__all__ = [
    "Status",
    "Repo",
    "Commit",
    "Committer",
    "Project",
    "Component",
    "Deployment",
]


class Status(str, Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    PENDING = "pending"


@dataclass
class Repo:
    owner: str
    name: str


@dataclass
class Committer:
    username: str
    email: str


@dataclass
class Commit:
    ref: str
    sha: str


@dataclass
class Project:
    repo: Repo
    committer: Committer
    commit: Commit


# responses
@dataclass
class Component:
    name: str
    url: str


@dataclass
class Deployment:
    id: str
    manifest: str
    project: str
    status: Status
    logs: Optional[str] = None
    components: Optional[list[Component]] = field(default_factory=list)


@dataclass
class Project:
    id: str
    repo: str