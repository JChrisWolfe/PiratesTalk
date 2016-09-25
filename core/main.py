from network.pirateservice import PirateService


def main():
    user_wants_to_continue = "Y"
    while user_wants_to_continue == "Y":
        pirateservice = PirateService()
        input_text = input("Please enter the text to be translated: ")
        pirate_text = pirateservice.send_pirate_request(input_text)
        print("The translated text is: ")
        print(pirate_text)
        user_wants_to_continue = continue_translating_text()


"""
    Checking if the user wants to translate another sentence. To be on the safe side,
    the loop will continue only if the user enters Y/y
"""
def continue_translating_text():
    user_wants_to_continue = input("Do you want to translate another sentence[Y/N]? ")
    if user_wants_to_continue not in ("Y", "N", "y", "n"):
        print("Invalid option. Exiting the app")
        user_wants_to_continue = "N"

    return user_wants_to_continue

main()