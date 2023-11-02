from stegano import lsb
def main() :
    secret = lsb.hide("./RickAstley.png", "Never gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt youNever gonna give you upNever gonna let you downNever gonna run around and desert youNever gonna make you cryNever gonna say goodbyeNever gonna tell a lie and hurt you")
    secret.save("./RickWithSecret.png")
    clear_message = lsb.reveal("./RickWithSecret.png")
    print(clear_message)

if __name__ == '__main__':
    main()