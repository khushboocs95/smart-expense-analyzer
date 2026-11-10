import { useMemo } from "react";
import {
  Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis,
} from "recharts";
import { formatINR } from "../utils/format";

export default function CategoryChart({ data }: { data: Record<string, number> }) {
  const chartData = useMemo(
    () =>
      Object.entries(data)
        .map(([category, amount]) => ({ category, amount }))
        .sort((a, b) => b.amount - a.amount),
    [data]
  );

  return (
    <div className="panel">
      <h2>Spending by category</h2>
      <ResponsiveContainer width="100%" height={320}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" vertical={false} />
          <XAxis dataKey="category" />
          <YAxis tickFormatter={(v: number) => `₹${(v / 100000).toFixed(1)}L`} />
          <Tooltip formatter={(value) => formatINR(Number(value))} />
          <Bar dataKey="amount" fill="#4f46e5" radius={[6, 6, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}