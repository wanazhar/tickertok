// contracts/MarketMaker.sol
pragma solidity ^0.8.0;

contract AutonomousMM {
    mapping(string => uint256) public reserves;
    uint256 public constant FEE = 30; // 0.3%
    
    function swap(
        string memory fromAsset,
        string memory toAsset,
        uint256 amount
    ) external returns (uint256) {
        uint256 fromReserve = reserves[fromAsset];
        uint256 toReserve = reserves[toAsset];
        uint256 amountOut = (amount * toReserve) / (fromReserve + amount);
        reserves[fromAsset] += amount;
        reserves[toAsset] -= amountOut;
        return amountOut - (amountOut * FEE) / 10000;
    }
}