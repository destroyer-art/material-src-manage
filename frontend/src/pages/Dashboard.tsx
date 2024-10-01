import React from "react";
import { withMainLayout } from "../layouts";
import { InventoryTable } from "../components/Common";

export const Dashboard: React.FC = withMainLayout(() => {
  return <InventoryTable />;
});
