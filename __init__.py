import ngrok

from comfy.cli_args import args

# #########################################################
# Replace None on the line below this with your Authtoken.
# Your Authtoken can be found at https://dashboard.ngrok.com/get-started/your-authtoken
# Don't forget to enclose it in quotation marks!
# Example:
# ngrok_token = "DuMMyTOk3n38ty38nhbvgjbb_HEhdpnojhrbdpnrmE0jt"

ngrok_token = None

# #########################################################

print("### Load ngrok")

def connect():
    # Connect if ngrok token is set
    if ngrok_token is not None:
        print("trying to connect ngrok...\n")
        options = {"authtoken": ngrok_token, "session_metadata": "ComfyUI"}

        try:
            ngrok_url = ngrok.forward(f"{args.listen}:{args.port}", **options).url()
        except Exception as e:
            print("Failed to connect to ngrok.")
        else:
            print(f"\n\033[32m\033[1m##\n## Connection to ngrok established.\n##\n## URL: {ngrok_url}\n##\n\033[0m\033[0m")
            
connect()