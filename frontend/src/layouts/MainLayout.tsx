import { HeaderBarView } from "../components/Views";

interface MainLayoutProps {
  children: React.ReactNode;
}

const MainLayout: React.FC<MainLayoutProps> = ({ children }) => {
  return (
    <div className="w-full h-full relative">
      <HeaderBarView />
      <div className="w-full h-[calc(100vh-112px)]">{children}</div>
    </div>
  );
};

export const withMainlayout = (Page: React.FC) => () => {
  return (
    <MainLayout>
      <Page />
    </MainLayout>
  );
};
