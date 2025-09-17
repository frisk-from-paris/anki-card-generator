import cli
import loader
from anki.exports import export
from anki.builder import create_notes


def main():
    args = cli.parse()

    if args.file:
        data = loader.load_notes(args.file)
    else:
        data = loader.load_notes(args.directory)

    all_notes = create_notes(data, args.translate_to)
    export(args.name, all_notes, args.output)


if __name__ == "__main__":
    main()
