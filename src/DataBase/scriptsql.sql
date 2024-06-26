USE [master]
GO
/****** Object:  Database [BankingSystemProject]    Script Date: 14/02/1403 11:21:48 ق.ظ ******/
CREATE DATABASE [BankingSystemProject]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'BankingSystemProject', FILENAME = N'D:\SQL Server 2022\root\MSSQL16.MSSQLSERVER\MSSQL\DATA\BankingSystemProject.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'BankingSystemProject_log', FILENAME = N'D:\SQL Server 2022\root\MSSQL16.MSSQLSERVER\MSSQL\DATA\BankingSystemProject_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [BankingSystemProject] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [BankingSystemProject].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [BankingSystemProject] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [BankingSystemProject] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [BankingSystemProject] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [BankingSystemProject] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [BankingSystemProject] SET ARITHABORT OFF 
GO
ALTER DATABASE [BankingSystemProject] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [BankingSystemProject] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [BankingSystemProject] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [BankingSystemProject] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [BankingSystemProject] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [BankingSystemProject] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [BankingSystemProject] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [BankingSystemProject] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [BankingSystemProject] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [BankingSystemProject] SET  DISABLE_BROKER 
GO
ALTER DATABASE [BankingSystemProject] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [BankingSystemProject] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [BankingSystemProject] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [BankingSystemProject] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [BankingSystemProject] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [BankingSystemProject] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [BankingSystemProject] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [BankingSystemProject] SET RECOVERY FULL 
GO
ALTER DATABASE [BankingSystemProject] SET  MULTI_USER 
GO
ALTER DATABASE [BankingSystemProject] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [BankingSystemProject] SET DB_CHAINING OFF 
GO
ALTER DATABASE [BankingSystemProject] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [BankingSystemProject] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [BankingSystemProject] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [BankingSystemProject] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'BankingSystemProject', N'ON'
GO
ALTER DATABASE [BankingSystemProject] SET QUERY_STORE = ON
GO
ALTER DATABASE [BankingSystemProject] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [BankingSystemProject]
GO
/****** Object:  Table [dbo].[Account]    Script Date: 14/02/1403 11:21:49 ق.ظ ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Account](
	[account_number] [char](8) NOT NULL,
	[account_amount] [float] NOT NULL,
	[account_owner] [int] NULL,
 CONSTRAINT [PK_Account] PRIMARY KEY CLUSTERED 
(
	[account_number] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Bank]    Script Date: 14/02/1403 11:21:49 ق.ظ ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Bank](
	[bank_id] [int] NOT NULL,
	[name] [nvarchar](80) NULL,
 CONSTRAINT [PK_Bank] PRIMARY KEY CLUSTERED 
(
	[bank_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Branch]    Script Date: 14/02/1403 11:21:49 ق.ظ ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Branch](
	[branch_id] [int] NOT NULL,
	[name] [nvarchar](80) NULL,
	[number_of_customers] [int] NULL,
	[budget] [float] NULL,
	[city_name] [nvarchar](80) NULL,
	[bank_id] [int] NULL,
 CONSTRAINT [PK_Branch] PRIMARY KEY CLUSTERED 
(
	[branch_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[customer]    Script Date: 14/02/1403 11:21:49 ق.ظ ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[customer](
	[national_code] [int] NOT NULL,
	[first_name] [nvarchar](80) NULL,
	[family_name] [nvarchar](80) NULL,
	[home_town] [nvarchar](80) NULL,
 CONSTRAINT [PK_customer] PRIMARY KEY CLUSTERED 
(
	[national_code] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Loan]    Script Date: 14/02/1403 11:21:49 ق.ظ ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Loan](
	[loan_number] [int] NOT NULL,
	[loan_amout] [float] NULL,
	[customer_id] [int] NULL,
	[account_id_int] [int] NULL,
	[branch_id] [int] NULL,
	[account_id] [char](8) NULL,
 CONSTRAINT [PK_Loan] PRIMARY KEY CLUSTERED 
(
	[loan_number] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[test_for_python]    Script Date: 14/02/1403 11:21:49 ق.ظ ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[test_for_python](
	[id] [int] NOT NULL,
	[name] [nvarchar](50) NULL,
 CONSTRAINT [PK_test_for_python] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Account]  WITH CHECK ADD  CONSTRAINT [account_owner] FOREIGN KEY([account_owner])
REFERENCES [dbo].[customer] ([national_code])
GO
ALTER TABLE [dbo].[Account] CHECK CONSTRAINT [account_owner]
GO
ALTER TABLE [dbo].[Branch]  WITH CHECK ADD  CONSTRAINT [FK_Branch_Bank] FOREIGN KEY([bank_id])
REFERENCES [dbo].[Bank] ([bank_id])
GO
ALTER TABLE [dbo].[Branch] CHECK CONSTRAINT [FK_Branch_Bank]
GO
ALTER TABLE [dbo].[customer]  WITH CHECK ADD  CONSTRAINT [FK_customer_customer] FOREIGN KEY([national_code])
REFERENCES [dbo].[customer] ([national_code])
GO
ALTER TABLE [dbo].[customer] CHECK CONSTRAINT [FK_customer_customer]
GO
ALTER TABLE [dbo].[Loan]  WITH CHECK ADD  CONSTRAINT [FK_Loan_Branch] FOREIGN KEY([branch_id])
REFERENCES [dbo].[Branch] ([branch_id])
GO
ALTER TABLE [dbo].[Loan] CHECK CONSTRAINT [FK_Loan_Branch]
GO
ALTER TABLE [dbo].[Loan]  WITH CHECK ADD  CONSTRAINT [FK_Loan_customer_account_id] FOREIGN KEY([account_id])
REFERENCES [dbo].[Account] ([account_number])
GO
ALTER TABLE [dbo].[Loan] CHECK CONSTRAINT [FK_Loan_customer_account_id]
GO
ALTER TABLE [dbo].[Loan]  WITH CHECK ADD  CONSTRAINT [FK_Loan_customer1] FOREIGN KEY([customer_id])
REFERENCES [dbo].[customer] ([national_code])
GO
ALTER TABLE [dbo].[Loan] CHECK CONSTRAINT [FK_Loan_customer1]
GO
USE [master]
GO
ALTER DATABASE [BankingSystemProject] SET  READ_WRITE 
GO
