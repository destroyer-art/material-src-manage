import React, { useEffect, useState } from "react";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  TablePagination,
} from "@mui/material";
import { Inventory } from "../../types";
import axios from "axios";

export const InventoryTable: React.FC = () => {
  const [inventory, setInventory] = useState<Inventory[]>([]);
  const [page, setPage] = useState<number>(0);
  const [rowsPerPage, setRowsPerPage] = useState<number>(10);

  const fetchData = async () => {
    const response = await axios.get("http://localhost:4000/inventory", {
      params: { page: page + 1, perpage: rowsPerPage },
    });
    const data: Inventory[] = response.data;
    return data;
  };

  useEffect(() => {
    fetchData().then((data) => setInventory(data));
  }, [page, rowsPerPage]);

  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  return (
    <Paper sx={{ width: "100%", overflow: "hidden" }}>
      <TableContainer>
        <Table stickyHeader aria-label="data table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Product Number</TableCell>
              <TableCell>Form</TableCell>
              <TableCell>Grade</TableCell>
              <TableCell>Finish</TableCell>
              <TableCell>Quantity</TableCell>
              <TableCell>Weight</TableCell>
              <TableCell>Location</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {inventory
              .map((ivntry) => (
                <TableRow hover role="checkbox" tabIndex={-1} key={ivntry.id}>
                  <TableCell>{ivntry.id}</TableCell>
                  <TableCell>{ivntry.product_number}</TableCell>
                  <TableCell>{`${ivntry.form} ${ivntry.choice}`}</TableCell>
                  <TableCell>{`${ivntry.grade} ${ivntry.surface}`}</TableCell>
                  <TableCell>{ivntry.finish}</TableCell>
                  <TableCell>{ivntry.quantity}</TableCell>
                  <TableCell>{ivntry.weight}</TableCell>
                  <TableCell>{ivntry.location}</TableCell>
                </TableRow>
              ))}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[5, 10, 15]}
        component="div"
        count={11650}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
  );
};
