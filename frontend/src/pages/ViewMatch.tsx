import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { PATH } from "../consts";
import { Preference } from "../types";

export const ViewMatchPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const [preference, setPreference] = useState<Preference[]>([]);

  useEffect(() => {
    if (!location.state) {
      navigate(PATH.DASHBOARD);
    }
    setPreference(location.state);
  }, [preference]);

  return <>Hello, World</>;
};
