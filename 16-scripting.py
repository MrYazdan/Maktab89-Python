import argparse
import translators.server as tss

# fa_text = "سلام دوستان عزیزم !"
# print(tss.google(fa_text, from_lang="fa", to_lang="en"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Translator Script v0.1")

    parser.add_argument('file_path', nargs="?", action="store")
    parser.add_argument('-f', '--from-lang', action="store", default="auto")
    parser.add_argument('-t', '--to-lang', action="store", required=True)
    parser.add_argument('-p', '--provider', action="store", default="google", choices=[
        "google", "yandex", "sogou", "bing", "tencent", "alibaba"
    ])
    parser.add_argument('-s', '--save', default=None)

    args = parser.parse_args()
    text = ""

    if not args.file_path:
        try:
            while True:
                text += input(": ") + "\n"
        except KeyboardInterrupt:
            print()

    else:
        with open(args.file_path) as f:
            text = f.read()

    from_lang, to_lang, provider = args.from_lang, args.to_lang, args.provider
    translated_text = getattr(tss, provider)(text, from_lang, to_lang)

    if args.save:
        with open(args.save, "w") as f:
            f.write(translated_text + "\n")

        print("Result saved in :", args.save)
    else:
        print("Result : \n", translated_text, sep="")



