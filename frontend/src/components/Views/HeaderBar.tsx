import React from "react";
import { AppBar, Toolbar, Typography, Container } from "@mui/material";

export const HeaderBarView: React.FC = () => {
  return (
    <AppBar
      position="sticky"
      sx={{
        zIndex: 20,
        minHeight: '4rem',
        maxHeight: '4rem',
        background: 'linear-gradient(90deg, #5c5e75, #100c35)',
        boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.3)',
      }}
    >
      <Container maxWidth="xl">
        <Toolbar
          sx={{
            display: 'flex',
            justifyContent: 'space-between',
            paddingY: '1.375rem',
          }}
        >
          <Typography variant="h6" component="div" sx={{ flexGrow: 1, paddingX: 1 }}>
            Inventory Management
          </Typography>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
