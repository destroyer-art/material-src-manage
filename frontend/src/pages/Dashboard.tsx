import React from "react";
import { withMainlayout } from "../layouts";
import { InventoryTable } from "../components/Common";

export const Dashboard: React.FC = withMainlayout(() => {
  return <InventoryTable />;
});
