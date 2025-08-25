import { useState } from 'react'
import Button from './components/Button'
import ProgressBar from './components/ProgressBar'

export default function App() {
  const [step, setStep] = useState(0)

  return (
    <div className="max-w-xl mx-auto p-4">
      <ProgressBar step={step} total={7} />
      {step === 0 ? (
        <div className="text-center space-y-4">
          <h1 className="text-2xl font-bold">Find Your Best-Fit City & Lifestyle</h1>
          <p className="text-gray-600">Take a quick assessment to see which Indian cities match your vibe.</p>
          <Button onClick={() => setStep(1)}>Start My Assessment</Button>
        </div>
      ) : (
        <div className="text-center">Assessment coming soon...</div>
      )}
    </div>
  )
}
