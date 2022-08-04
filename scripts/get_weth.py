from brownie import accounts, config, network, interface

def main():
    """
    Runs the get_weth function to get WETH
    """
    get_weth()

def get_weth(account=None):
    """
    Mints WETH by depositing ETH.
    """
    account = (
        account if account else accounts.add(config["wallets"]["from_key"])
    )  # add your keystore ID as an argument to this call

    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    #decimals = weth.decimals()
    tx = weth.deposit({"from": account, "value": 0.1 * 1e18})
    #tx = weth.deposit({"from": account, "value": 10000000000000000})
    print("\nReceived 0.1 WETH\n")
    #print(f"\nweth name {weth.allowance()}\n")
    return tx



