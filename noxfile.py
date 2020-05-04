# noxfile.py
import nox


locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.7"])
def tests(session):
    """Run the test suite."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "pytest", "--cov", external=True)


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
