
data = {
	"ID":
	{
		"I00000000000000000001":
		{
			"key": "0z8YmIROEn9tMCMnyjzOI",
			"transactions":
			{
				#For testing
				0:
				{
					"from": "I00000000000000000002",
					"amount": 50
				}
			}
		},

		"I00000000000000000002":
		{
			"key": "0Yr8QJBD4iui9aZV7NsxR",
			"transactions":
			{

			}
		}	
	}
}


def get_amount_data(ID):
	
	total_amount = 0

	for transaction_data in data["ID"][ID]["transactions"].values():
		
		try:
			transaction_data["to"]
			total_amount -= transaction_data["amount"]
			
		except KeyError:

			if transaction_data["from"]:
				total_amount += transaction_data["amount"]

	return total_amount


def get_transaction_data(ID):

	return data["ID"][ID]["transactions"]


def get_transaction_id(ID):

	return len(data["ID"][ID]["transactions"])


def new_transaction(p, ID, amount):

	if p == "sender":
		return {"to": ID, "amount": amount}
	elif p == "receiver":
		return {"from": ID, "amount": amount}


class Sender:

	__senderID = ""
	priv_key   = ""

	def __init__(self, senderID):

		self.__senderID = senderID


	def send(self, receiverID, amount):

		try:
			if data["ID"][self.__senderID]["key"] == self.priv_key:

				if get_amount_data(self.__senderID) >= amount:

					try:
						sender_transaction_id   = get_transaction_id(self.__senderID)
						receiver_transaction_id = get_transaction_id(receiverID)

						sender_new_transaction   = new_transaction("sender", receiverID, amount)
						receiver_new_transaction = new_transaction("receiver", self.__senderID, amount)

						data["ID"][self.__senderID]["transactions"].update({sender_transaction_id: sender_new_transaction})
						data["ID"][receiverID]["transactions"].update({receiver_transaction_id: receiver_new_transaction})

						print("Transaction successful.")

					except KeyError:

						print(f"Sending Failed: ID {receiverID} does not exist.")
				else:
					print(f"Sending Failed: Unsufficient balance: {get_amount_data(self.__senderID)}")
			else:
				print(f"Sending Failed: Key {self.priv_key} is wrong.")

		except KeyError:

			print(f"Sending Failed: ID {self.__senderID} does not exist.")


print(f"""
Sender transaction data before sending:     {get_transaction_data("I00000000000000000001")}
Receiver transaction data before receiving: {get_transaction_data("I00000000000000000002")}

Sender amount data before sending:          {get_amount_data("I00000000000000000001")}
Receiver amount data before receiving:      {get_amount_data("I00000000000000000002")}
""")


sender = Sender("I00000000000000000001")  #SenderID

sender.priv_key = "0z8YmIROEn9tMCMnyjzOI" #SenderKey

sender.send("I00000000000000000002", 10)  #ReceverID, amount


print(f"""
Sender transaction data after sending:      {get_transaction_data("I00000000000000000001")}
Receiver transaction data after receiving:  {get_transaction_data("I00000000000000000002")}

Sender amount data after sending:           {get_amount_data("I00000000000000000001")}
Receiver amount data after receiving:       {get_amount_data("I00000000000000000002")}
""")
