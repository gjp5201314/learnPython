import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "@/components/Layout";
import Home from "@/pages/Home";
import Learn from "@/pages/Learn";
import Lesson from "@/pages/Lesson";
import Progress from "@/pages/Progress";
import Practice from "@/pages/Practice";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="/learn" element={<Learn />} />
          <Route path="/learn/:stageId" element={<Learn />} />
          <Route path="/lesson/:lessonId" element={<Lesson />} />
          <Route path="/progress" element={<Progress />} />
          <Route path="/practice" element={<Practice />} />
          <Route path="*" element={<Home />} />
        </Route>
      </Routes>
    </Router>
  );
}
