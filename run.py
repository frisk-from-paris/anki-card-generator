import cli
import loader
from anki import utils


def main():
    args = cli.parse()

    data = loader.load_notes(args.directory)
    all_notes = utils.create_notes(data)

    utils.export(args.name, all_notes, args.output)


if __name__ == "__main__":
    main()
