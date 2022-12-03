import React, { useEffect, useState } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

const SERVER_PREFIX =
  "http://ec2-13-215-211-254.ap-southeast-1.compute.amazonaws.com";

const getData = (id) => {
  return fetch(`${SERVER_PREFIX}/user/bankaccounts`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ userid: id }),
  });
};

const Home = () => {
  const [data, setData] = useState([]);
  const userid = 1;

  useEffect(() => {
    getData(userid)
      .then((res) => res.json())
      .then((body) => {
        setData(body.data);
      });
  }, []);

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Account&nbsp;ID</TableCell>
            <TableCell align="right">Account Type</TableCell>
            <TableCell align="right">AccountBalance</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row) => (
            <TableRow
              key={row.AccountID}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.AccountID}
              </TableCell>
              <TableCell align="right">{row.AccountType}</TableCell>
              <TableCell align="right">{row.AccountBalance}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default Home;
