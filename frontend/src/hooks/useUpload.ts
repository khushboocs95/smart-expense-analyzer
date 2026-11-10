import { useMutation } from "@tanstack/react-query";
import axios from "axios";
import type { UploadResult } from "../type";

const API_URL = "http://127.0.0.1:8000";

export function useUpload() {
  return useMutation({
    mutationFn: async (file: File): Promise<UploadResult> => {
      const formData = new FormData();
      formData.append("file", file);
      const { data } = await axios.post<UploadResult>(`${API_URL}/upload`, formData);
      return data;
    },
  });
}