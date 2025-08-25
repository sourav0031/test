export default function ProgressBar({ step, total }) {
  const percent = Math.round((step / total) * 100)
  return (
    <div className="w-full bg-gray-200 rounded-full h-2 mb-4">
      <div
        className="bg-blue-600 h-2 rounded-full transition-all"
        style={{ width: `${percent}%` }}
      />
    </div>
  )
}
