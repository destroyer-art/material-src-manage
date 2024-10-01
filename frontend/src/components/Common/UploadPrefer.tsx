import { UploadFile } from "@mui/icons-material";
import { Box, Button } from "@mui/material";
import React, { ChangeEvent, useState } from "react";

interface CSVData {
    [key: string]: string;
  }
  
  const parseCSV = (csvText: string): CSVData[] => {
    const lines = csvText.split("\n").map((line) => line.trim());
    if (lines.length < 2) return [];
  
    const headers = lines[0].split(",");
    const rows: CSVData[] = lines.slice(1).map((line) => {
      const values = line.split(",");
      return headers.reduce<CSVData>((acc, header, index) => {
        acc[header.trim()] = values[index]?.trim() || "";
        return acc;
      }, {});
    });
  
    return rows;
  };

export const UploadPrefer: React.FC = () => {
  const [csvData, setCsvData] = useState<CSVData[]>([]);

  const handleFileUpload = (event: ChangeEvent<HTMLInputElement>): void => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const csvText = e.target?.result as string;
        const parsedData = parseCSV(csvText);

        setCsvData(parsedData);
      };
      reader.readAsText(file);
    }
  };

  return (
    <Box display="flex" alignItems="center" sx={{ padding: 2 }}>
      <Button
        variant="contained"
        component="label"
        startIcon={<UploadFile />}
        sx={{ marginRight: 2 }}
      >
        Upload CSV
        <input type="file" accept=".csv" hidden onChange={handleFileUpload} />
      </Button>
    </Box>
  );
};
