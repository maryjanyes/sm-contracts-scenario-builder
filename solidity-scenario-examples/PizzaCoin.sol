// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract PizzaCoin {
  address public owner = msg.sender;
  address public lastPizzaBuyer;
  uint public pizzasCount;

  error NotEnoughFunds(uint requested, uint available);

  mapping(address => int) supplierBalances;
  mapping(address => int) balances;

  modifier onlyOwner() {
    require(
      msg.sender == owner,
      "This function is restricted to the contract's owner"
    );
    _;
  }

  function orderPizza(int amount, address supplier) public {
    supplierBalances[supplier] += amount;
    balances[msg.sender] -= amount;
  }
}
