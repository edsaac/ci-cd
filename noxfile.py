import argparse

import nox


@nox.session(reuse_venv=True)
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "--serve" to serve.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--serve", action="store_true", help="Serve after building")
    args, posargs = parser.parse_known_args(session.posargs)

    session.install("-e.[docs]")
    session.chdir("docs")

    session.run(
        "sphinx-build",
        "-b",
        "html",
        ".",
        f"_build/html",
        *posargs,
    )

    if args.serve:
        session.log("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
        session.run("python", "-m", "http.server", "8000", "-d", "_build/html")

