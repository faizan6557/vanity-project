import boto3
import string

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VanityNumbers")

# Phone number -> letters mapping
digit_to_letters = {
    "2": "ABC", "3": "DEF", "4": "GHI",
    "5": "JKL", "6": "MNO", "7": "PQRS",
    "8": "TUV", "9": "WXYZ"
}

def lambda_handler(event, context):
    caller = event.get("callerNumber", "")
    
    # Generate vanity numbers (simple example: replace last 3 digits with letters)
    vanity_list = []
    for d in caller[-3:]:
        if d in digit_to_letters:
            vanity_list.append(caller[:-3] + digit_to_letters[d][0:1])
    
    # Top 3 vanity numbers (demo ke liye simple pick)
    top3 = vanity_list[:3]

    # Save to DynamoDB
    table.put_item(
        Item={
            "callerNumber": caller,
            "vanityNumbers": top3
        }
    )

    return {
        "callerNumber": caller,
        "vanityNumbers": top3
    }
