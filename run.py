import cli
import loader
from anki.exports import export
from anki.builder import create_notes


def main():
    args = cli.parse()
    source_path = args.file if args.file else args.directory

    data = loader.load_notes(source_path)
    all_notes = create_notes(data, args.translate_to)

    # run the deck export
    export(args.name, all_notes, args.output)


if __name__ == "__main__":
    main()
