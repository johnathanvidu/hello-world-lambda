def lambda_handler(event, context):
    from layer_dependency import say_hello
    say_hello()
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda'
    }
