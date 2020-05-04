# noxfile.py
import nox


@nox.session(python=["3.8", "3.7"])
def tests(session):
    """Run the test suite."""
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")