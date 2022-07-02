from brownie import simplestorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]  # grabbing an account
    # Act - deploy
    simple_storage = simplestorage.deploy({
        "from": account
    })
    starting_value = simple_storage.retrieve()

    # Assert- check
    expected = 0
    assert starting_value == expected


def test_update():
    # Arrange
    account = accounts[0]
    # Act - update
    simple_storage = simplestorage.deploy({
        "from": account
    })
    update = simple_storage.store(15, {
        "from": accounts[1]
    })
    check = simple_storage.retrieve()
    print(check)
    # Assert - Check

    expected = 15
    assert check == expected