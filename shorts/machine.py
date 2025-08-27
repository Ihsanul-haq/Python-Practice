emoticon = "v.v"
def main():
    global emoticon
    say("Is there anyone?")
    emoticon = ":D"
    say("oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)

main()