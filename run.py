import cli
import loader
from anki import utils


def main():
    args = cli.parse()

    if args.file:
        data = loader.load_notes(args.file)
    else:
        data = loader.load_notes(args.directory)
    print(data)
    all_notes = utils.create_notes(data)

    utils.export(args.name, all_notes, args.output)


if __name__ == "__main__":
    main()
