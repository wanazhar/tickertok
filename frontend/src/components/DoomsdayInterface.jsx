// src/components/DoomsdayInterface.jsx
import { ApocalypseCounter } from '@terminal-killer/ui';
import { BloodMarketChart } from '@vampire-charts/core';
import { SoulTradeInterface } from '@underworld-finance/react';

export default function TerminalKillerUI() {
  return (
    <div className="doomsday-terminal">
      <ApocalypseCounter targets={['BLOOMBERG', 'EIKON']} />
      <BloodMarketChart 
        depth={666} 
        darkMode="hellfire"
      />
      <SoulTradeInterface 
        maxLeverage={1000}
        soulCollateral={true}
      />
      <LiquidityVampireControls />
      <MarketAssassinDashboard />
    </div>
  )
}