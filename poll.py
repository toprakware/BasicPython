#Toprk

class Poll:

    _choice_dict = {}
    _vote_count = {}
    _total_vote_count = 0

    def __init__(self, title: str, MAX_OPTION=5, default_s=4):
        self.title = title
        self.MAX_OPTION = MAX_OPTION
        self.default_s = default_s

    def add_options(self):

        __index = 0
        while True:
            choice = input(f"\nAdd an Option (MIN 2, MAX {self.MAX_OPTION}) (Type done/DONE to complete the Addition part): ")

            if choice in ("done","DONE"):
                if len(self._choice_dict) < 2:
                    print("You can add MIN 2 options.")
                    continue
                else:
                    return True

            if choice == "":
                print("\nYou cannot use BLANK name.")
                continue

            self._choice_dict[__index] = choice
            self._vote_count[__index] = 0
            __index += 1

            if len(self._choice_dict) > self.MAX_OPTION - 1:
                    print(f"You can add MAX {self.MAX_OPTION} Options.\n")
                    return True

                
    def _calc_p(self, n):
        return round((self._vote_count[n]/self._total_vote_count)*100)


    def _print_poll(self, ended=False):
        longest_string = max(self._choice_dict.values(), key=len)

        print("\n  ------------------------------------")
        print(f"    {self.title}")
        print("  ------------------------------------")
        
        for i in range(len(self._choice_dict)):
            s = len(longest_string) + self.default_s - len(self._choice_dict[i])

            try:

                print("  ------------------------------------")
                print(" "*self.default_s, i+1,  self._choice_dict[i], " "*s + "|", self._vote_count[i], "|" + " "*self.default_s + "%", self._calc_p(i))
                print("  ------------------------------------")           
            except ZeroDivisionError:
                print(" "*self.default_s, i+1, self._choice_dict[i], " "*s  + "|", self._vote_count[i], "|" + " "*self.default_s + "%0")
                print("  ------------------------------------")

        if ended:
            print(f"   {self._total_vote_count} votes | Poll ended.\n")
        else:
            print(f"   {self._total_vote_count} votes\n")


    def vote(self):

        while True:

            self._print_poll()
            vote_index = input("Please select who to vote for ('Q' to Quit): ")

            try:
                int(vote_index)
            except ValueError:
                if vote_index == "Q":
                    self._print_poll(ended=True)
                    quit()
                else:
                    print(f"\nPlease use numbers between 1-{len(self._choice_dict)}")
                    continue

            try:
                self._vote_count[int(vote_index) - 1] += 1
            except KeyError:
                print(f"\nPlease use numbers between 1-{len(self._choice_dict)}")
                continue

            self._total_vote_count += 1

poll = Poll("EPIC BOSS FIGHT WHO WILL WIN")

if poll.add_options():
    poll.vote()
