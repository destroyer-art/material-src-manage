import { UploadFile } from "@mui/icons-material";
import { Box, Button } from "@mui/material";
import axios from "axios";
import React, { ChangeEvent, useState } from "react";
import { Preference } from "../../types";

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

const addPreferToDB = async (csvData: CSVData[]) => {
  const obj = { abc: 12 };
  const formattedData: Preference[] = csvData.map(
    (csv) =>
      ({
        material: csv["Material"],
        form: csv["Form"],
        grade: csv["Grade"],
        choice: csv["Choice"],
        min_width: parseFloat(csv["Width (Min)"]),
        max_width: parseFloat(csv["Width (Max)"]),
        min_thickness: parseFloat(csv["Thickness (Min)"]),
        max_thickness: parseFloat(csv["Thickness (Max)"]),
      })
  );

  await axios.post("http://localhost:4000/preference", formattedData);
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
        addPreferToDB(parsedData);
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
